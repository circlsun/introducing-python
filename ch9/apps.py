def nonbuggy(arg, result=None):
    if not result:
        result = []
    result.append(arg)
    return result


print(nonbuggy(5))
print(nonbuggy(6))
print(nonbuggy(7))
print(nonbuggy(8))
