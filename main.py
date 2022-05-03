import copy

import LinkedList
import random

names = ["glenn", "vic", "brian", "michelle", "john", "vanessa", "nirosh"] ## list of names
names_out_order = copy.deepcopy(names)

root = LinkedList.Node(names[0], None) ## start of list
names.remove(names[0])
current_node = root ## finds first person and their target

while len(names) != 0:
    rand_num = random.randint(0, len(names) - 1) ## a random number that is between 0 and length of names
    current_node.target = LinkedList.Node(names[rand_num], None) ## setting a target to a random name
    names.remove(names[rand_num]) ## removes the set name from list
    current_node = current_node.target ## sets iterator to the next target

for current_name in names_out_order: ## to create text files with targets assigned to names
    current_node = root ## resets iterator to root so we dont run into the end before finding all names
    while current_node.name != current_name: ## loop until the name in the node is equal to current name
        current_node = current_node.target ## node is updated with target
    with open(current_name + ".txt", 'w+') as f: ## create text file
        f.write("your super secret assignment is to assasinate ") ## writes "your super secret..."
        if (current_node.target == None): ## if the node gets to the end of the list
            f.write(root.name) ## node gets assigned root name (first name) as target
        else: ## if anything else happens other than above
            f.write(current_node.target.name) ## write current node's target name
        f.close() ## close file