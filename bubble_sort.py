# Question: Write a Python program to implement the Bubble Sort algorithm from scratch 
# to sort a list of numbers in ascending order without using the built-in .sort() method.

# Solution: Bubble Sort Implementation in Python

def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        swapped = False
        
        # Last i elements are already in place, so we don't need to check them
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                
        # If no two elements were swapped in the inner loop, the list is already sorted
        if not swapped:
            break
            
    return arr

# Test the function
numbers = [64, 34, 25, 12, 22, 11, 90]
print(f"Original list: {numbers}")

sorted_numbers = bubble_sort(numbers)
print(f"Sorted list using Bubble Sort: {sorted_numbers}")