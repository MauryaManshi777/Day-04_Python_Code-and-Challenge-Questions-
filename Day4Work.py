#### **** (Mixed List & Tuple) **** ######

#1.Create a list and convert it into a tuple.
my_list = [1,2,3,44,5,7,"mm"]
my = tuple(my_list)
print(my)

#2.Create a tuple and convert it into a list.
my_tuple = (1,2,3,4.87,"mm")
my = list(my_tuple)
print(my)

#3.Find the maximum element in both a list and a tuple.
list_element = [1,2,3,44,5,7]
tuple_element = (1,2,3,44,55,7)
le = max(list_element)
te = max(tuple_element)
print(f"Maximum of List: {le}\nMaximum of Tuple: {te}")

#4.Find the minimum element in both a list and a tuple.
list_element = [1,2,3,44,5,7]
tuple_element = (0,2,3,44,55,7)
le = min(list_element)
te = min(tuple_element)
print(f"Minimum of List: {le}\nMinimum of Tuple: {te}")

#5.Find the sum of elements in a list and a tuple.
list_element = [1,2,3,4,5,7]
tuple_element = (0,2,3,4,5,7)
print("Sum of the list: ",sum(list_element))
print("Sum of the tuple",sum(tuple_element))

#6.Take 5 numbers as input, store them in a list, then convert the list into a tuple and print both.
l = []

a1 = int(input("Enter number: "))
a2 = int(input("Enter number: "))
a3 = int(input("Enter number: "))
a4 = int(input("Enter number: "))
a5 = int(input("Enter number: "))

l.append(a1)
l.append(a2)
l.append(a3)
l.append(a4)
l.append(a5)

print(l)

t = tuple(l)
print(t)

#7.Merge two lists.
list1 = [1,3,45,7,5]
list2 = [12,13,14,15,77]
list1.extend(list2)
print(list1,list2)

#8.Merge two tuples.
tu1 = (1,3,45,7,5)
tu2 = (12,13,14,15,77)
# The '+' operator combines them into a new tuple
tu3 = tu1+tu2
print("Merged Tuple:", tu3)
print("Original tu1:", tu1)  ## tu1 stays exactly the same

#9.Find common elements between two lists.
list1 = [1,2,3,4,58]
list2 = [1,2,3,4,5,8,76,45]
mm = set(list1).intersection(set(list2))

count = len(mm)

print("Common elements: ",mm)
print("Total count: ",count)

#10.Remove duplicate elements from a list.
numbers = [1,2,3,4,58,1,58,7,77,74,76,76,74,4]
## set() removes duplicates instantly
remove_element= list(set(numbers))

print(remove_element)

#### ***Challenge Questions ****  #####

#11.Store the names of 10 students in a list and print them alphabetically.
student = ["Manshi Maurya","Ashutosh Maurya","Gudiya Maurya","Khuboo Maurya","Aditya Maurya",
           "Simran","Mansim","Ritika","Khuboo Singh","Khushi Singh"]
name = sorted(student)
print(name)

#12.Store the marks of 5 students and find the highest marks.
student = [83,56,78,45,100]
student.sort()
print(student)

#13.Store the marks of 5 students and find the average marks.
student_mark = [25,33,28,40,50]
mark = sum(student_mark) /len(student_mark)
print(f"The average mark is: {mark}")

#14.Create a tuple of months and ask the user to enter a month number (1–12). Print the corresponding month.
month = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
print(month)

print_month = int(input("Enter month number (1-12): "))
print(f"Print the corresponding month: {month[print_month -1]}")

#15.Create a shopping list. Allow the user to:
#•Add an item. 
#•Remove an item. 
#•Display all items. 

# Initial shopping list
shoping_list = ["1 kg rice", "2 kg dal", "1 kg khana"]

# --- 1. DISPLAY THE INITIAL LIST ---
print("Current Shopping List:")
print(*shoping_list, sep="\n")

# --- 2. ADD AN ITEM ---
new_item = input("\nEnter an item to add: ")
shoping_list.append(new_item)

# Display updated list
print("\nList After Adding:")
print(*shoping_list, sep="\n")

# --- 3. REMOVE AN ITEM ---
# Note: The user must type an exact item from the list above, or Python will show an error.
item_to_remove = input("\nEnter the exact item to remove: ")
shoping_list.remove(item_to_remove)

# --- 4. DISPLAY FINAL LIST ---
print("\nFinal Shopping List:")
print(*shoping_list, sep="\n")


