with open('/Users/xavierloffree2/Downloads/input.txt') as f:
    lines = f.readlines()

max_count = [0,0,0]
count = 0
for num in lines:
    if num == "\n":
        if count > min(max_count):
            max_count.remove(min(max_count))
            max_count.append(count)
            count = 0
        else:
            count = 0
    else:
        count = count + int(num)


print(sum(max_count))