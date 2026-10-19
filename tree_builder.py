from platform import node


class EmployeeNode:
    '''
    A class to represent a node in the binary tree.
    Attributes:
        name (str): The name of the employee.
        left (EmployeeNode): The left child node, representing the left subordinate.
        right (EmployeeNode): The right child node, representing the right subordinate.
    '''
    #Base class for binary tree node
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

class TeamTree:
    '''
    A class to represent a binary tree for managing a team structure.
    Attributes:
        root (EmployeeNode): The root node of the tree, representing the team lead.
    Methods:
        insert(manager_name, employee_name, side, current_node=None): Inserts a new employee under the specified manager.
        print_tree(node=None, level=0): Prints the tree structure starting from the given node.

    '''
    
    #Constructor for TeamTree class
    def __init__(self):
        self.root = None
    
    #Prints whatever is in tree structure
    def print_tree(self, node=None, level=0):
            if node is None:
                if level == 0:
                    node = self.root
                    if node is None:
                        print("No team lead found. Please add a team lead first.")
                        return
                else:
                    return
    
            indent = "    " * level
            print(f"{indent}- {node.name}")
            
            # Recursive cases
            self.print_tree(node.left, level + 1) 
            self.print_tree(node.right, level + 1)
    
    def insert(self, manager_name, employee_name, side, current_node=None):
        #If nothing in tree
        if self.root is None:
            print("No team lead found. Please add a team lead first.")
            return

        if current_node is None:
            current_node = self.root

        #If current node is correct manager, add employee to selected side
        if current_node.name == manager_name:
            if side == "left" and current_node.left is None:
                current_node.left = EmployeeNode(employee_name)
                print(f"{employee_name} added to the LEFT of {manager_name}.")
            elif side == "right" and current_node.right is None:
                current_node.right = EmployeeNode(employee_name)
                print(f"{employee_name} added to the RIGHT of {manager_name}.")
            else:
                print(f"{manager_name} already has an employee on the {side}.")
            return
        
        #If current node not manager, search subtrees
        found_left = False
        found_right = False
        
        if current_node.left:
            found_left = self.insert(manager_name, employee_name, side, current_node.left)
        if current_node.right:
            found_right =self.insert(manager_name, employee_name, side, current_node.right)
            
        #If manager not found in either subtree
        if not found_left and not found_right:
            if current_node == self.root:
                print(f"Manager {manager_name} not found in the team structure.")
            return False
        return True

#Nodes for tree structure
root = EmployeeNode("Manager")
employee = EmployeeNode("Employee")
side = EmployeeNode("Side Employee")

#tree hierarchy
root.left = employee
root.right = employee
side.left = employee
side.right = employee

tree = TeamTree()
tree.root = root

# CLI functionality
def company_directory():
    tree = TeamTree()

    while True:
        print("\n📋 Team Management Menu")
        print("1. Add Team Lead (root)")
        print("2. Add Employee")
        print("3. Print Team Structure")
        print("4. Exit")
        choice = input("Choose an option (1–4): ")

        if choice == "1":
            if tree.root:
                print("⚠️ Team lead already exists.")
            else:
                name = input("Enter team lead's name: ")
                tree.root = EmployeeNode(name)
                print(f"✅ {name} added as the team lead.")

        elif choice == "2":
            manager = input("Enter the manager's name: ")
            employee = input("Enter the new employee's name: ")
            side = input("Should this employee be on the LEFT or RIGHT of the manager? ")
            side = side.lower()
            tree.insert(manager, employee, side)

        elif choice == "3":
            print("\n🌳  Current Team Structure:")
            tree.print_tree()

        elif choice == "4":
            print("Good Bye!")
            break
        else:
            print("❌ Invalid option. Try again.")
            
company_directory()

'''
recursive insertions worked by checking if the current node is the manager, if not it recursively checks the left and right subtrees until it finds the manager or reaches a child node. If the manager is found, it adds the employee to the specified side. If not found, it returns False and prints a message indicating that the manager was not found in the team structure.
Some of the challenges I faced when finding the right spot for a new employee involved ensuring that the tree structure remained valid and that employees were not added to a side that was already occupied. I also had to handle cases where the manager wasn't found in the tree, requiring careful traversal of the tree to ensure all nodes were checked. Additionally, I had to manage the user input for the side (left or right) and ensure that it was correctly interpreted and validated before attempting to insert the new employee.
Trees might be preferrable to other data structures in real world systems because they allow for hierarchical representation of data, which is common in organizational structures. Trees provide efficient searching and insertion operations when balanced, and they can represent relationships between entities in a clear and intuitive way.
'''