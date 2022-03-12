print('x y z w')
for y in 0, 1:
    for x in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (not(x) or y or z) and (x or not(z) or not(w))
                        if not(F):
                        print(x, y, z, w)
