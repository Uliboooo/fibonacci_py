def write_csv(n, count):
    with open('fibonacci.csv', 'a') as c:
        c.write(str(count) + "," + str(n) + ",\n")
        print("\r" + str(count) + "回書き込み", end="")

while True:
    #設定の入力
    print("1. n番目を求めますか?\n2. n番目番目まで全ての値を求めますか?\n1か2を入力してください。")
    All_cal = False
    chosen_input = input()
    if chosen_input == "1":
        All_cal = False
    else:
        All_cal = True
    print("nの値を入力してください。")
    time_cal = int(input())
    #データの初期化
    list_fibonacci = [0,1,]
    with open('fibonacci.csv', 'w') as c:
        c.write("time" + "," + "value" + ",\n")
    # 演算
    count = 1
    for i in range(time_cal - 2):
        list_fibonacci.append(list_fibonacci[i]+list_fibonacci[i + 1])
        i -= 1
        print("\r" + str(count) + "回演算", end="")
        count += 1
    print("演算終了")
    #出力
    if All_cal == False:
        print(list_fibonacci[len(list_fibonacci) - 1])
    else:
        # 書き込み
        count = 1
        for n in list_fibonacci:
            write_csv(n, count)
            count += 1
        print("\n書き込み完了")
    print("もう1度計算しますか?y/n")
    if input() != "y":
        break