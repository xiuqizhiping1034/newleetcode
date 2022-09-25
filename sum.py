a = int(input('input'))

for i in range(a):
    # 调节数字前方空格数量
    # 可针对层数为一位数、两位数的金字塔打印
    if i < 10:
        print(' '*(a - 8) + '  '*(a + 1 - i), end='')
    else:
        print('   ' * (a + 1 - i), end='')
    # 输出金字塔左半部分（包括0）
    j = i
    while j != -1:
        print(j+1, end=' ')
        j = j - 1
    # 输出金字塔右半部分（不包括0）
    j = 1
    while j != i+1:
        print(j+1, end=' ')
        j = j + 1

    print()