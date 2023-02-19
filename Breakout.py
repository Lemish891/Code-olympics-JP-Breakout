import itertools
import numpy as np

def permutationsofgroup(lst):
    return list(itertools.permutations(lst))


def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))

names = ["Scott", "Robbie", "Jo", "Lewis", "Lewis_2","Adam","Copey","Marina","Ben"]
friends = [["Lewis","Robbie","Adam","Copey"],["Scott","Jo","Marina"],
           ["Robbie","Lewis_2","Marina"],["Scott","Lewis_2","Adam","Copey"],["Jo","Lewis","Ben"],["Scott","Lewis","Copey"],["Scott","Lewis","Adam"],["Robbie","Jo"],["Ben"]]

group_size = 3

if len(names) % group_size == 0:
    number_of_groups = int(len(names)/group_size)
else:
    number_of_groups = (len(names)//group_size) + 1

perms = permutationsofgroup(names)
perm_sizes = []
for p in perms:
    perm_sizes.append(list(split(p,number_of_groups)))

score = 0
best_perm = []
for perm in perm_sizes:
    perm_score = 0
    for group in perm:
        for i in group:
            friend_list = friends[names.index(i)]
            for friend in friend_list:
                if friend in group:
                    perm_score -= 1
                else:
                    perm_score += 1
    if perm_score > score:
        score = perm_score
        best_perm = perm

print(best_perm)