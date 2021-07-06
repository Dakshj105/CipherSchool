def CombinationOfNumber(s, n, i = 0):
    if i ==(n - 1):
        print("".join(s), end = " ")
        return

    for j in range(i, n):
        s[i], s[j] = s[j], s[i]
        CombinationOfNumber(s, n, i + 1)
        s[j], s[i] = s[i], s[j]

s = [i for i in input()]
CombinationOfNumber(s, len(s))
