import re


prop_line_regex = re.compile(r'^>\s+<([^>]+)>')


def molblocks(filename):
    with open(filename) as f:
        molblock = ''
        for l in f:
            molblock += l
            if l == '$$$$\n':
                yield molblock
                molblock = ''


def extract_props(molblock):
    props = {}
    prop_name = None
    for l in molblock.split("\n"):
        if prop_name is not None:
            props[prop_name] = l
            prop_name = None
        else:
            m = prop_line_regex.match(l)
            if m is not None and len(m.groups()) > 0:
                prop_name = m.group(1)
    return props


def printraw(*args):
    print(*args, end='')


def sum(filename):
    i = 0
    summary = {}
    for molblock in molblocks(filename):
        i += 1
        props = extract_props(molblock)
        for k in props.keys():
            if k not in summary:
                summary[k] = 0
            summary[k] += 1

    print("Total: {}".format(i))
    print("Properties:")
    for k, v in summary.items():
        print("  {}: {}".format(k, v))


def grep(filename, pattern, invert):
    for molblock in molblocks(filename):
        props = extract_props(molblock)
        match = any([re.search(pattern, k) for k in props.keys()])
        if not invert and match:
            printraw(molblock)
        elif invert and not match:
            printraw(molblock)


def head(filename, limit=10):
    i = 0
    for molblock in molblocks(filename):
        printraw(molblock)
        i += 1
        if i == limit:
            break
