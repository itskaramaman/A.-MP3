# One common way of digitalizing sound is to record sound intensity at particular time moments. For each time moment intensity is recorded as a non-negative integer. Thus we can represent a sound file as an array of n non-negative integers.

# If there are exactly K distinct values in the array, then we need k=⌈log2K⌉ bits to store each value. It then takes nk bits to store the whole file.

# To reduce the memory consumption we need to apply some compression. One common way is to reduce the number of possible intensity values. We choose two integers l≤r, and after that all intensity values are changed in the following way: if the intensity value is within the range [l;r], we don't change it. If it is less than l, we change it to l; if it is greater than r, we change it to r. You can see that we lose some low and some high intensities.

# Your task is to apply this compression in such a way that the file fits onto a disk of size I bytes, and the number of changed elements in the array is minimal possible.

# We remind you that 1 byte contains 8 bits.

# k=⌈log2K⌉ is the smallest integer such that K≤2k. In particular, if K=1, then k=0.

# Input
# The first line contains two integers n and I (1≤n≤4⋅105, 1≤I≤108) — the length of the array and the size of the disk in bytes, respectively.

# The next line contains n integers ai (0≤ai≤109) — the array denoting the sound file.

# Output
# Print a single integer — the minimal possible number of changed elements.

# Examples
# inputCopy
# 6 1
# 2 1 2 3 4 3
# outputCopy
# 2
# inputCopy
# 6 2
# 2 1 2 3 4 3
# outputCopy
# 0
# inputCopy
# 6 1
# 1 1 2 2 3 3
# outputCopy
# 2
# Note
# In the first example we can choose l=2,r=3. The array becomes 2 2 2 3 3 3, the number of distinct elements is K=2, and the sound file fits onto the disk. Only two values are changed.

# In the second example the disk is larger, so the initial file fits it and no changes are required.

# In the third example we have to change both 1s or both 3s.


from collections import Counter
from math import log2

n, i = map(int, input().split())
x = list(map(int, input().split()))
cnt = Counter(x)
i = i*8
count = 0


def calcSize(cnt):
    k = log2(len(cnt))
    return n*k


def check(i, cnt):
    if i >= calcSize(cnt):
        return True
    else:
        return False


def removeItem(item, x):
    while item in x:
        x.remove(item)
    return x


while not check(i, cnt):
    minx = min(cnt)
    maxx = max(cnt)
    if cnt[minx] < cnt[maxx]:
        if cnt[minx] != 0:
            cnt[minx] -= 1
            count += 1
        else:
            removeItem(minx, x)
            cnt = Counter(x)
    else:
        if cnt[maxx] != 0:
            cnt[maxx] -= 1
            count += 1
        else:
            removeItem(maxx, x)
            cnt = Counter(x)

print(count)
