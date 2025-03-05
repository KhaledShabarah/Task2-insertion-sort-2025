def selection_sort_ages(ages):
    sorted_ages = ages.copy()
    
    n = len(sorted_ages)
    
    for i in range(n):
        min_index = i
        
        for j in range(i+1, n):
            if sorted_ages[j] < sorted_ages[min_index]:
                min_index = j
        
        sorted_ages[i], sorted_ages[min_index] = sorted_ages[min_index], sorted_ages[i]
    
    return sorted_ages

def main():
    students_ages = [22, 19, 25, 18, 20, 23, 21, 24]
    
    print("Original ages: ", students_ages)
    
    sorted_ages_asc = selection_sort_ages(students_ages)
    print("Ages in ascending order: ", sorted_ages_asc)
    
    sorted_ages_desc = sorted_ages_asc[::-1]
    print("Ages in Descending order: ", sorted_ages_desc)
    
    print("Oldest age: ", sorted_ages_asc[0])
    print("Youngest age: ", sorted_ages_asc[-1])
    print("Ages Avg: ", round(sum(students_ages) / len(students_ages), 2))

main()
