#funcation rotate(arr[],d,n) that rotates arr[] of size n by d elements.
# E.g [1,2,3,4,5] After 2 rotations [4,5,1,2,3]

def rotate(arr,d,n):
    """
    Since rotations are cyclic, reduce the number of rotations if greater than size of array by finding remainder.
    Split the list/array at the number of rotations.
    Join the two parts (2nd part + 1st part).
    """
    no_of_rotations = d%n
    part_1 = arr[:no_of_rotations]
    part_2 = arr[no_of_rotations:]
    return part_2 + part_1

arr = [1,2,3,4,5,6,7,8,9,10]

print(rotate(arr,15,10))
