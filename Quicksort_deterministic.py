import random
def median_of_three(arr, low, high):
    
    mid = (low + high) // 2
    pivot = sorted([arr[low], arr[mid], arr[high]])[1]
    return pivot

def quicksort(arr, low, high):
    if low >= high:
        return
    
    pivot = median_of_three(arr, low, high)
    #pivot=random.choice(arr)
    
    i = low
    j = high
    
    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
            
    # Now `j` is the last index of the left partition
    quicksort(arr, low, j)
    quicksort(arr, i, high)

# Example usage
arr = [8, 7, 0, 2, 1, 9,7,6,2,6,4,5,88,99,66,332,2,-1]
quicksort(arr, 0, len(arr) - 1)
print(arr)  # Should output the sorted array
