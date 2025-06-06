from random import randint

s = 0
ss = randint(1, 13)
if ss >= 10:
    ss = 10
if s <= 10 and ss == 1:
    ss = 11
s += ss

d = 0
dd = randint(1, 13)
if dd >= 10:
    dd = 10
if d <= 10 and dd == 1:
    dd = 11
d += dd

print(f"Dealer má {d} a jednu další kartu")

dd = randint(1, 13)
if dd >= 10:
    dd = 10
if d <= 10 and dd == 1:
    dd = 11
d += dd

while True:
    ss = randint(1, 13)
    if ss >= 10:
        ss = 10
    if s <= 10 and ss == 1:
        ss = 11
    s += ss
    if s > 21:
        print(f"Máš {s}, prohrál jsi!")
        exit()
    else:
        if input(f"Máš {s}, chceš další kartu? ANO/NE ") == "NE":
            break

while d < 17:
    print(f"Dealer  má  {d}")
    dd = randint(1, 13)
    if dd >= 10:
        dd = 10
    if d <= 10 and dd == 1:
        dd = 11
    d += dd
print(f"Dealer má {d}")

if d > s:
    print("Dealer má více a proto vyhrál")
elif s < d:
    print("Máš více, než dealer, vyhrál jsi!")
elif b:
    print("Dealer má blackajck, vyhrál")
else:
    print()