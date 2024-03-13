print("ass. no.2 in data science")

###1. Write a NumPy program to test whether none of the elements of a given array is zero.
import numpy as np

def non_zeros(arr):
    return np.all(arr !=0)

array_x = np.array([1,2,3,4,5,6])
array_y = np.array([1,2,3,4,5,0])

print("array 1 :", array_x)
print("non of the elements are zero :" , non_zeros(array_x))

print("array 2 :", array_y)
print("non of the elements are zero :" , non_zeros(array_y))


print("#"*50)

###2. Write a NumPy program to test whether any of the elements of a given array is non-zero.
import numpy as np
def not_zero(arr):
    return np.any(arr !=0)

arr1 = np.array([0,0,0,0,0,0,0]) 
arr2 = np.array([0,1,0,0,4,0,6]) 

print("first array :", arr1)
print("any of the elements are not zero :", not_zero(arr1))

print("second array :", arr2)
print("any of the elements are not zero :", not_zero(arr2))


print("#"*50)

###3. Write a NumPy program to create an element-wise comparison (equal, equal within a tolerance) of two given
import numpy as np

def elementwise_comparison( arr1 , arr2 , tolerance = None ):
    if tolerance is None:
        return arr1 == arr2
    else:
        return np.isclose(arr1, arr2, atol = tolerance)
 
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([1, 2, 3, 4, 5])
arr3 = np.array([1.001, 2.002, 3.003, 4.004, 5.005])

print("Array 1:", arr1)
print("Array 2:", arr2)

print("Element-wise comparison (equal):", elementwise_comparison(arr1, arr2))

print("\nArray 1:", arr1)
print("Array 3:", arr3)

print("Element-wise comparison (equal within a tolerance):", elementwise_comparison(arr1, arr3, tolerance=0.01)) 


print("#"*50)

###4. Write a NumPy program to create an array of 10 zeros,10 ones, 10 fives.
import numpy as np 

#an array of 10 zeros
zeros_arr = np.zeros(10)

#an array of 10 ones
ones_arr  = np.ones(10)

#an array of 10 fives
fives_arr = np.ones(10)*5

print("the array of 10 zeros : ",zeros_arr)
print("the array of 10 ones  : ",ones_arr)
print("the array of 10 fives : ",fives_arr)


print("#"*50)

###5. Write a NumPy program to create an array of the integers from 30 to70.
import numpy as np

integers_arr = np.arange(30 , 71)

print("the integers_arr from 30 to 70 :",integers_arr)


print("#"*50)

###6. Write a NumPy program to create a 3x3 identity matrix
import numpy as np
matrex = np.eye(3)
print("==> 3*3 identity matrex :")
print("\n ",matrex)


print("#"*50)

###7. Write a NumPy program to generate a random number between 0 and 1 
import numpy as np
random_no = np.random.random()
print("random number between 1 and 10 : ", random_no)

print("#"*50)

###8. Write a NumPy program to generate an array of 15 random numbers from a standard normal distribution 
import numpy as np 
random_arr = np.random.randn(15)
print("array of 15 random numbers from a standard normal distribution :")
print("\n" ,random_arr)


print("#"*50)

###9. Write a NumPy program to create a vector with values ranging from 15 to 55 and print all values except the first and last.
import numpy as np 
vector = np.arange(15 , 56)
print("all values of the vestor except the first and last one : " , vector[1:-1])


print("#"*50)

###10. Write a NumPy program to create a vector of length 5 filled with arbitrary integers from 0 to 10
import numpy as np
vector = np.random.randint(0 , 11 , size = 5)
print("Vector of length 5 filled with arbitrary integers from 0 to 10 :")
print("\n\t\t\t\t\t\t\t\t " , vector)


print("#"*50)

###11. Write a NumPy program to create a 10x10 matrix, in which the elements on the borders will be equal to 1, and inside 0.
import numpy as np
# Create a 10x10 matrix filled with zeros
matrix = np.zeros((10, 10))
# Set the border elements to 1
matrix[0, :] = 1  # Top row
matrix[-1, :] = 1  # Bottom row
matrix[:, 0] = 1  # Leftmost column
matrix[:, -1] = 1  # Rightmost column

print("10x10 Matrix with border elements equal to 1 and interior elements equal to 0:")
print("\n",matrix)


print("#"*50)

###12. Write a NumPy program to create a 5x5 zero matrix with elements on the main diagonal equal to 1, 2, 3, 4, 5.
import numpy as np
# Create a 5x5 zero matrix
matrix = np.zeros((5, 5))
# Assign values to the main diagonal
np.fill_diagonal(matrix, [1, 2, 3, 4, 5])
print(matrix)

print("#"*50)

###13. Write a NumPy program to create a 4x4 matrix in which 0 and 1 are staggered, with zeros on the main diagonal
import numpy as np
# Create a 4x4 matrix filled with zeros
matrix = np.zeros((4, 4), dtype=int)
# Fill the matrix with staggered 0s and 1s
matrix[::2, 1::2] = 1
matrix[1::2, ::2] = 1
print(matrix)

print("#"*50)

###14. Write a NumPy program to save two given arrays into a single file in compressed format (.npz format) and load it.
import numpy as np
## Two arrays to save
array1 = np.array([[1, 2, 3], [4, 5, 6]])
array2 = np.array([[7, 8, 9], [10, 11, 12]])
## Save the arrays into a single compressed file
np.savez_compressed('arrays.npz', array1=array1, array2=array2)
## Load the arrays from the compressed file
loaded_data = np.load('arrays.npz')
## Access the arrays by their keys
loaded_array1 = loaded_data['array1']
loaded_array2 = loaded_data['array2']
print("Array 1:")
print(loaded_array1)
print("\nArray 2:")
print(loaded_array2)

print("#"*50)

###15. Write a NumPy program to create a one-dimensional array of forty pseudo-randomly generated values. Select 
import numpy as np
# Generate a one-dimensional array of forty pseudo-random values
random_array = np.random.rand(40)
# Select specific elements from the array
selected_values = random_array[[2, 5, 8, 10, 15, 20, 25, 30, 35]]
print("Generated random array:")
print(random_array)
print("\nSelected values:")
print(selected_values)

print("#"*50)

###16. Write a NumPy program to extract all numbers from a given array which are less and greater than a specified number
import numpy as np

def extract_numbers(array, specified_number):
    # Extract numbers less than the specified number
    less_than = array[array < specified_number]
    
    # Extract numbers greater than the specified number
    greater_than = array[array > specified_number]
    
    return less_than, greater_than

# Example array
arr = np.array([1, 5, 10, 15, 20, 25])
# Specified number
specified_number = 10
# Extract numbers less and greater than the specified number
less_than_specified, greater_than_specified = extract_numbers(arr, specified_number)
print("Array:", arr)
print("Numbers less than", specified_number, ":", less_than_specified)
print("Numbers greater than", specified_number, ":", greater_than_specified)

print("#"*50)










