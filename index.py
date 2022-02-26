countRef = 0
skip_count = []

while countRef <= 100:
    if countRef % 2 == 0:
        skip_count.append(countRef)
    countRef = countRef + 1

print(skip_count)
