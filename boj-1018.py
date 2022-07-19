import sys
input = sys.stdin.readline

n, m = map(int, input().split())
chess = [input().strip() for _ in range(n)]
ans = []

for i in range(n-7):
    for j in range(m-7):
        sww = 0 #start with white
        swb = 0 #start with black
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k + l) % 2 == 0:
                    if chess[k][l] != 'W':
                        sww += 1
                    if chess[k][l] != 'B':
                        swb += 1
                else:
                    if chess[k][l] != 'B':
                        sww += 1
                    if chess[k][l] != 'W':
                        swb += 1
        ans.append(min(sww, swb))
print(min(ans))