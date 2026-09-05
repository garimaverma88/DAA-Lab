# Bubble Sort
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] >arr[j + 1]:
arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break


# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
i = 0
    j = 0

    while i<len(left) and j <len(right):
        if left[i] <= right[j]:
result.append(left[i])
i += 1
        else:
result.append(right[j])
            j += 1

result.extend(left[i:])
result.extend(right[j:])

    return result


# Input data
best_case = [1, 2, 3, 4, 5]
average_case = [3, 1, 5, 2, 4]
worst_case = [5, 4, 3, 2, 1]

# Testing Bubble Sort
print("Bubble Sort:")
print("Best Case:", end=" ")
arr = best_case.copy()
bubble_sort(arr)
print(arr)

print("Average Case:", end=" ")
arr = average_case.copy()
bubble_sort(arr)
print(arr)

print("Worst Case:", end=" ")
arr = worst_case.copy()
bubble_sort(arr)
print(arr)

# Testing Merge Sort
print("\nMerge Sort:")
print("Best Case:", merge_sort(best_case.copy()))
print("Average Case:", merge_sort(average_case.copy()))
print("Worst Case:", merge_sort(worst_case.copy()))
