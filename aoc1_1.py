with open('/Users/xavierloffree2/Downloads/input.txt') as f:
    lines = f.readlines()

print(lines)
print(lines[1][:len(lines[1])-1])


max_count = 0
count = 0
for num in lines:
    if num == "\n":
        if count > max_count:
            max_count = count
            count = 0
        else:
            count = 0
    else:
        count = count + int(num)

print(max_count)

