 # Tuple to store winning positions
win_positions = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
)

def game(player):
    # Display current mesh
    print("\n", " | ".join(mesh[:3]))
    print("---+---+---")
    print(" ", " | ".join(mesh[3:6]))
    print("---+---+---")
    print(" ", " | ".join(mesh[6:]))

    # Loop until player enters a valid input
    while True:
        try:
            ch = int(input(f"Enter player {player}'s choice : "))
            if ch < 1 or ch > 9 or mesh[ch - 1] in (player1, player2):
                raise ValueError
            mesh[ch - 1] = player
            break
        except ValueError:
            print("Invalid position number.")

    # Return winning positions if player wins, else None
    for wp in win_positions:
        if all(mesh[pos] == player for pos in wp):
            return wp
    return None

player1 = "X"
player2 = "O"
player = player1
mesh = list("123456789")

for i in range(9):
    won = game(player)
    if won:
        print("\n", " | ".join(mesh[:3]))
        print("---+---+---")
        print(" ", " | ".join(mesh[3:6]))
        print("---+---+---")
        print(" ", " | ".join(mesh[6:]))
        print(f"*** Player {player} won! ***")
        break
    # Switch player
    player = player2 if player == player1 else player1
else:
    print("It's a draw!")
