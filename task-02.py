

def binary_search(arr, x):
    low = 0
    high = len(arr)-1
    mid = 0
    counter = 0

    while low <= high:

        counter += 1

        mid = (low + high) // 2

        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1

        else:
            return (counter, arr[mid])

    return (counter, arr[mid+1])


x = 1.23

sorted_array = [
    0.12, 0.45, 0.78, 1.23, 1.56, 1.89, 2.34, 2.67, 3.01, 3.45,
    3.89, 4.12, 4.56, 4.89, 5.23, 5.67, 6.01, 6.45, 6.78, 7.12,
    7.56, 7.89, 8.23, 8.67, 9.01, 9.34, 9.78, 10.12, 10.45, 10.89
]
result = binary_search(sorted_array, x)
print(result)
