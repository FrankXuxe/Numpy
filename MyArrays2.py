import numpy as np
import random

#row = student, col = exam
grades = np.array([[87, 96, 70], [100, 87, 90], [94, 77, 90], [100, 81, 82]])

student1 = grades[1]

student0_test1 = grades[0, 1]

# upper bound is not included
stuent0_1 = grades[0:2]

student1and3 = grades[[1, 3]]

# to select students 1 and 3 but only test 2
students1and3_test2 = grades[[1, 3], 2]

all_students_test0 = grades[:, 0]

all_students_test2 = grades[:, 1:3]

all_students_test0and2 = grades[:, [0, 2]]

grades = np.random.randint(60, 100, 12).reshape(3, 4)

grades.mean()
# Colomn Average
grades.mean(axis=0)
# Row Average
grades.mean(axis=1)

# shallow and original are correlated

number = np.arange(1, 6)

number_view = number.view()

number[1] *= 10

number_view[1] /= 10

number_slice = number[0:3]

number[1] *= 20

# Deep copy are not affect when change the original

number_copy = number.copy()

number[1] *= 10

grades = np.array([[87, 96, 70], [100, 87, 90]])

# Reshape method produces a shallow copy
grades_reshaped = grades.reshape(1, 6)
# Resize just change the original
grades.resize(1, 6)

# glatten creates a deep copy, just one dimentional

flattened = grades.flatten()

# Ravel creats a shallow copy

raveled = grades.ravel()

raveled[0] = 100

flattened[1] = 100

print()
