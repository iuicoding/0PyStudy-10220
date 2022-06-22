score = float(input("별점을 입력하세요."))
print(score)
if score == 5:
    print("완벽")
elif 4.5 <= score:
    print("매우 만족")
if not (score == 5):
    print("5가 아니다")
if score == 5 and score - 1 == 4:
    print("점수는 5가 맞네")
if 2 <= 3:
    print("2 <= 3")

alist = [1, 2, 3, 4, 5]

print(alist)

if 4 in alist:
    print("4가 있네")

if 121 not in  alist:
    print("121없음 뭐임")

print(alist[1])

alist = alist + [1]
alist = alist * 2
alist.append(8)
print(alist)

del alist[0]
alist.remove(2)
alist.pop(4)
alist.pop()
print(alist)

print(alist + [2])
print(alist * 3)

for element in alist:
    print(element)