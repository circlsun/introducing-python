def buggy(arg, result=[]):
    result.append(arg)
    return result


def nonbuggy(arg, result=[]):
    if not result:
        result = []
    result.append(arg)
    return result


print(buggy(5))
print(buggy(6))
print(buggy(7))
print(buggy(8))

print(nonbuggy(5))
print(nonbuggy(6))
print(nonbuggy(7))
print(nonbuggy(8))
