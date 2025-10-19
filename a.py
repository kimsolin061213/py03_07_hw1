# %%

a = list(map(int, input('숫자 5개 입력').split()))
a.append(input('문자 1개 입력'))
print(a)

# %%

a = list(map(int, input('숫자 5개 입력').split()))
del a[-2:]
print(a)

# %%

a = list(map(int, input('숫자 5개 입력').split()))
for index, nn in enumerate(a, start = 101):
  print(index, nn)

# %%

a = [10, 20, 30, 40, 30, 20, 10]
nn = a.count(20)
print(nn)

# %%

a = list(map(int, input('숫자 10개 입력').split()))
n = min(a)
x = max(a)
print(n, 'end', x)

# %%

a = list(map(int, input('숫자 10개 입력').split()))
a.sort()
nn = sum(a[1:-1])
print(nn)

# %%

a = [10, 20, 30, 40, 30, 20, 10]
while 20 in a:
  a.remove(20)
print(a)

# %%

a = [i for i in range(1, 6)]
print(a)

# %%

a = [i for i in range(1, 21) if i % 2 != 0]
print(a)

# %%

a, b = map(int, input('1-20과 10-30인 정수 두개 입력').split(''))
nn = [2 ** i for i in range(a, b + 1)] # 2를 i번 만큼 곱하기, (첫번째~두번째, +1 끝포함)
del nn[1]
del nn[-2]
print(nn)

# %%

a = input('Hello, world! 입력')
a = a.replace('Hello', 'hi')
print(a)

# %%

a = input('문자 4개 입력')
a = " / ".join(a)
print(a)

# %%

a = input('성씨 영문자 입력')
b = a.lower()
c = b.rjust(10)
print(c)

# %%

a = list(map(int, input('물품 가격 입력').split(';')))
a.sort()
for i in a:
  print('{0:>9}'.format(i))