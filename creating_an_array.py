import numpy as np

a = np.array([[1,2,3], [4,5,6]])
print(a)
print(f'dtype: {a.dtype}')
print(f'shape: {a.shape}')
print(f'length: {len(a)}')

print('zeros')
print(np.zeros((2,3)))
print('ones:')
print(np.ones((2,3)))



print(np.arange(start=0, stop =2, step = 0.5))
print(np.linspace(start=0, stop=1.5, num=4))

print(np.random.random((2,3)))


# indexing and slicing
a = np.arange(9)
a.shape = 3,3
print(a)

print(a[1,2])
print(a[1])

print(a[1:3])


print(a[:,1:3])



