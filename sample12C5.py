import itertools, random, bisect


class WeightedRandomGenerator(object):
    def __init__(self, weights):
        self.totals = []
        running_total = 0

        for obj in weights:
            running_total += weights[obj]
            self.totals.append(running_total)

    def next(self):
        rnd = random.random() * self.totals[-1]
        return bisect.bisect_right(self.totals, rnd)

    def __call__(self):
        return self.next()


with open("prob2.txt") as f:
    lines = f.readlines()
obj_dict = {}
obj_list = []
for i, l in enumerate(lines):
    p = l.find(" ")
    obj = l[p+1:].strip()
    cnt = int(l[:p])
    obj_dict[obj] = cnt
    obj_list.append(obj)

w = WeightedRandomGenerator(obj_dict)

total = 0
appeared = {}
results = []
while total < 1000:
    cur = []
    while len(cur) < 5:
        obj = w.next()
        if obj not in cur:
            cur.append(obj)
    if (2 in cur) and (0 not in cur) and (1 not in cur):
        continue
    cur.sort()
    s = ",".join(list(map(lambda x:str(x), cur)))
    #print(s)
    #if s in appeared:
    #    continue
    appeared[s] = True
    res = ",".join(list(map(lambda x: obj_list[x], cur))) + "\n"
    #print(res)
    total += 1
    results.append(res)

with open("results2.csv", "w") as f:
    f.writelines(results)
