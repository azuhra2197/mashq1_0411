# 1
kvadratlar = [x**2 for x in range(1, 11)]
print(kvadratlar)

# 2
juft_sonlar = [x for x in range(1, 21) if x % 2 == 0]
print(juft_sonlar)

# 3
toq_sonlar = [son for son in range(1, 31) if son % 2 != 0]
print(toq_sonlar)

# 4
uzunlik = ['aaple', 'banana', 'pear']
print(len(uzunlik))

# 5
harflar = list('soz')
print(harflar)

# 6
kublar = [x**3 for x in range(1, 6)]
print(kublar)

# 7
sozlar = ['dog', 'cat', 'mouse']
bosh_harflar = [soz[0] for soz in sozlar]
print(bosh_harflar)

# 8
sonlar = [1, 4, -9, 7, -5]
musbat_sonlar = [x for x in sonlar if x > 0]
print(musbat_sonlar)

# 9
royxat = []

for son in range(1, 11):
    if son % 2 == 0:
        belgisi = 'juft'
    else:
        belgisi = 'toq'
    royxat.append((son, belgisi))

print(royxat)

# 10
import math

sonlar = [4, 9, 16, 25]
ildizlar = [math.sqrt(son) for son in sonlar]

print(ildizlar)
