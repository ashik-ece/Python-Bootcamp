"""List Basics:
    - List AKA Array
    - Lists are Mutable - they can be changed
    - lists -> []
    - lists are 0 based index.
    - If lets say we wanted to add sugar in the below ingrediens, in case of tuples, that is not possible
    but in case of lists, it is possible to mutate or change the values  
"""
ingredients = ["water", "milk", "black tea"]
ingredients.append("Sugar") #used to add value (adds only to the end of it)
print(f"Ingredients are : {ingredients}")
ingredients.remove("water") #used to remove value
print(f"Ingrediens are : {ingredients}")

spice_options = ["ginger", 'cardamom']
chai_ingredients = ['water', "milk"]

#to add spice to our chai, we use "extend"

chai_ingredients.extend(spice_options)
print(f"chai: {chai_ingredients}")

#to insert a value anywhere in the array - "insert" (append adds the value always to the end)
#in insert, we have to provide what position we want to add

chai_ingredients.insert(2, "black Tea")
print(f"Chai : {chai_ingredients}")

# Remove and return item at the index specified (last item by default)
last_added = chai_ingredients.pop(2)
print(f"Chai : {last_added}")

# pop removes the item as well
print(f"Chai : {chai_ingredients}")

#reverse - It is a METHOD, it needs to be executed
# print(f"Chai : {chai_ingredients.reverse()}") # Output is NONE because its not returning anything.

#reverse doesnt return a new list, it reverses the mentioned list.
chai_ingredients.reverse()
print(f"Chai : {chai_ingredients}")

#to sort - sort

chai_ingredients.sort()
print(f"chaii : {chai_ingredients}")

# Passing lists to a function

# Print Maximum in a list

sugar_lvl = [1,2,3,4,5]
# max_lvl = max(sugar_lvl)
# print(f"max sugar lvl: {max_lvl}")
print(f"Maximum sugar level: {max(sugar_lvl)}") #this returns a new value/int, not as same as the reverse, so we can directly print it, reverse is the method, whereas max is a function.

#methods are tied to an object, whereas functions operate independently.

#to find minimum:
print(f"Minimum sugar level: {min(sugar_lvl)}")




