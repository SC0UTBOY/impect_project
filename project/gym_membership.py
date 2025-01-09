members = []

def add_member(members, member_id, name, age, membership, joining_date):
    member = {"id": member_id, "name": name, "age": age, "membership": membership, "joining_date": joining_date}
    members.append(member)
    print("Member added successfully!")

def search_member(members, member_id):
    for member in members:
        if member["id"] == member_id:
            return member
    return None

def update_membership(members, member_id, new_membership):
    for member in members:
        if member["id"] == member_id:
            member["membership"] = new_membership
            print("Membership updated successfully!")
            return
    print("Member not found!")

def delete_member(members, member_id):
    for i, member in enumerate(members):
        if member["id"] == member_id:
            members.pop(i)
            print("Member deleted successfully!")
            return
    print("Member not found!")

def display_members(members):
    print("ID\tName\t\tAge\tMembership\tJoining Date")
    for member in members:
        print(f"{member['id']}\t{member['name']}\t{member['age']}\t{member['membership']}\t{member['joining_date']}")

def sort_members_by_name(members):
    members.sort(key=lambda x: x["name"])
    print("Members sorted by name!")

def main_menu():
    while True:
        print("\n--- Member Management System ---")
        print("1. Add Member")
        print("2. Search Member")
        print("3. Update Membership")
        print("4. Delete Member")
        print("5. Display All Members")
        print("6. Sort Members by Name")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            member_id = input("Enter Member ID: ")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            membership = input("Enter Membership Type: ")
            joining_date = input("Enter Joining Date (YYYY-MM-DD): ")
            add_member(members, member_id, name, age, membership, joining_date)
        
        elif choice == "2":
            member_id = input("Enter Member ID to search: ")
            member = search_member(members, member_id)
            if member:
                print(f"Member found: {member}")
            else:
                print("Member not found!")
        
        elif choice == "3":
            member_id = input("Enter Member ID to update membership: ")
            new_membership = input("Enter new Membership Type: ")
            update_membership(members, member_id, new_membership)
        
        elif choice == "4":
            member_id = input("Enter Member ID to delete: ")
            delete_member(members, member_id)
        
        elif choice == "5":
            display_members(members)
        
        elif choice == "6":
            sort_members_by_name(members)
            display_members(members)
        
        elif choice == "7":
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main_menu()