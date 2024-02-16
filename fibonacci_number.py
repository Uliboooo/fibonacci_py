def write_csv(n, count):
    with open('fibonacci.csv', 'a') as c:
        c.write(str(count) + "," + str(n) + ",\n")
        print("\r" + str(count) + "回書き込み", end="")

list_fibonacci = [0,1,]
with open('fibonacci.csv', 'w') as c:
    c.write("time" + "," + "value" + ",\n")
# 演算
for i in range(100 - 2):
    list_fibonacci.append(list_fibonacci[i]+list_fibonacci[i + 1])
    i -= 1
print("演算終了")
# 書き込み
count = 1
for n in list_fibonacci:
    write_csv(n, count)
    count += 1

print("\n書き込み完了")