def buggy(arg, result=[]):
    result.append(arg)
    return result


def works(arg):
    result = []
    result.append(arg)
    return result


def nonbuggy(arg, result=[]):
    if result is None:
        result = []
    result.append(arg)
    return result


print(buggy(5))
print(buggy(6))
print(buggy(7))
print(buggy(8))
print()
print(works(5))
print(works(6))
print(works(7))
print(works(8))
print()
print(nonbuggy(5))
print(nonbuggy(6))
print(nonbuggy(7))
print(nonbuggy(8))
