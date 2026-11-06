from dateutil import parser
board1 = {
    "to do": [],
    "in progress": [],
    "done": []
  }

card_list = []

def find_card(board, title): #O(n)
    for column, cards in board.items():
        for card in cards:
            if card["title"].casefold() == title.casefold():
                return column, card
        print("no card found!")
        return None
                    
def add_card(board, title, assignee, due_date, description="", citations=None): #O(1)
    if citations is None:
        citations = []
    card = {
        "id": len(card_list),
        "title": title,
        "assignee": assignee,
        "description": description,
        "due date": due_date,
        "citations": citations
    }
    card_list.append(card)
    board["to do"].append(card)
    return

def edit_card(board, title, field, value): #O(1)
    find_card(board, title)[1][field] = value

    return

def move_card(board, title): #O(n)
    columns = list(board.keys())
    for i, column in enumerate(columns):
        if column == find_card(board, title)[0]:
            destination = columns[i+1]
            source = column
            board[destination].append(find_card(board, title)[1])
            board[source].remove(find_card(board, title)[1])
            break
    return

def prioritize_card(board, title): #O(1)
    card = find_card(board, title)[1]
    column = board[find_card(board, title)[0]]
    column.remove(card)
    column.insert(0, card)
    
    return
    

def delete_card(board, title): #O(1)
    board[find_card(board, title)[0]].pop(find_card(board, title)[1])

    return

def display_board(board): #O(n^2)
    for status in board:
       print(f"===={status.capitalize()}:====")
       for i, card in enumerate(board[status], start=1):
            print(f"{i}. {card['title']}\nAssigned: {card['assignee']}\nDue: {card['due date']}\nDescription: {card['description']}\nCitations:")
            for citation in card["citations"]:
                print(citation)
            print('\n')

def add_citation(board, title, citation): #O(1)
    find_card(board, title)[1]["citations"].append(citation)
    return

def binary_search(cards, target):
    if target < 0 or target >= len(cards):
        print("Card not found")
        return 
    low = 0
    high = len(cards) - 1

    while low < high:
        mid = low + (high-low)//2

        if cards[mid]:
            return cards[mid]

        elif cards[target]['id'] > cards[mid]['id']:
            low = mid + 1
        else:
            high = mid - 1
    print("Card not found")
    return 

def sort_by_due(cards):
    sbd_cards = cards.copy()
    n = len(sbd_cards)
    for i in range(n-1):
        for j in range(n - 1 - i):
            if sbd_cards[j]["due date"] > sbd_cards[j+1]["due date"]:
                sbd_cards[j]["due date"], sbd_cards[j+1]["due date"] = (
                    sbd_cards[j+1]["due date"], sbd_cards[j]["due date"]
                    )
    return sbd_cards

def find_card_by_id(cards, card_id):
    step_counter = 0
    if card_id < 0 or card_id >= len(cards):
            print("Card not found")
            return -1
    low = 0
    high = len(cards) - 1

    while low < high:
        step_counter += 1
        mid = low + (high-low)//2

        if cards[mid]:
            return cards[mid]

        elif cards[card_id]['id'] > cards[mid]['id']:
            low = mid + 1
        else:
            high = mid - 1
    print("Card not found")
    return None

def filter_by_assignee(board, assignee_name): 
    filtered_cards = set()
    for column, cards in board.items():
        for card in cards:
            if card["assignee"].casefold() == assignee_name.casefold():
                filtered_cards.add((column, card))

    if not filtered_cards:
        print(f"No cards found assigned to '{assignee_name}'.")
    return filtered_cards

while True:
    print("choose an option\n[1] Add Card  [2] Edit Card [3] Prioritize Card [4] Move Card [5] Delete Card [6] Add Citation [7] Sort by Due Date [8] Find Card by ID [9] Filter by Assignee [10] Exit Program")
    match int(input()):
        case 1:
            add_card(board1, input("Title: "), input("Assignee: "),parser.parse(input("Due Date: ")).date(), input("Description: "))
        case 2:
            edit_card(board1, input("Title: "), input("Field: "), input("New Value: "))
        case 3:
            prioritize_card(board1, input("Title: "))
        case 4:
            move_card(board1, input("Title: "))
        case 5:
            if input("Are you sure? [y/n]: ") == 'y':
                delete_card(board1, input ("Title: "))
        case 6:
            add_citation(board1, input("Title: "), input("Citation: "))
        case 7:
            display_board(sort_by_due([card for cards in board1.values() for card in cards]))
        case 8:
            column, card = find_card_by_id(card_list, int(input("Card ID: ")))
            if card:
                print(f"Card found in column '{column}':")
                for key, value in card.items():
                    print(f"{key.capitalize()}: {value}")
        case 9:
            filtered_cards = filter_by_assignee(board1, input("Assignee Name: "))
            for column, card in filtered_cards:
                print(f"Card found in column '{column}':")
                for key, value in card.items():
                    print(f"{key.capitalize()}: {value}")
        case 10:
            break
    display_board(board1)
    
            
            
            
