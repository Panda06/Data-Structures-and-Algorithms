# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

result = 0
max_index1 = max_index2 = -1
for i in range(0, n):
	if (max_index1 == -1) or a[i] > a[max_index1]:
		max_index1 = i
		
for i in range(0, n):
	if (i != max_index1) and ((max_index2 == -1) or a[i] > a[max_index2]):
		max_index2 = i	
result = a[max_index1] * a[max_index2]		
print(result)
