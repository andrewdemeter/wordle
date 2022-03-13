import mysql.connector

# Connect to database containing 5-letter words
connection = mysql.connector.connect(
    user="",
    password="",
    host="",
    database=""
)

# Create cursor to help execute query below
cursor = connection.cursor()

# Execute SQL query that randomly chooses word from database
cursor.execute("SELECT * FROM words ORDER BY RAND() limit 1")

# Fetch SQL query result and convert random word to string
sql_result = str(cursor.fetchone())

# Close database connection
connection.close()

# Reformat random word to exclude ()', characters
exclude = "()',"
answer = sql_result.translate((str.maketrans('', '', exclude)))

# Initialize player's guess count
guess_count = 0

# Create list of words that correspond with guess count
guess_count_words = ["first", "second", "third", "fourth", "fifth", "final"]

# Initialize guess variable so loop below works on first iteration
guess = "XXXXX"

# Continue looping until player solves answer or exhausts six guesses...
while guess.upper() != answer and guess_count <= 5:

    # Ask player to enter guess
    guess = input("\nPlease enter your " + guess_count_words[guess_count] + " guess...\n")

    # Continue looping until guess is five letters and doesn't include numbers or symbols...
    while len(guess) != 5 or guess.isalpha() is False:

        if len(guess) != 5 and guess.isalpha() is False:
            guess = input("Your guess must be five letters and cannot contain numbers or symbols. Try again...\n")

        elif len(guess) != 5:
            guess = input("Your guess must be five letters. Try again...\n")

        elif guess.isalpha() is False:
            guess = input("Your guess cannot contain numbers or symbols. Try again...\n")

    # Increase player's guess count by one
    guess_count += 1

    # Initialize position variable to use in loop below
    position = 0

    # Create empty list to store color boxes that correspond to each letter in player's guess
    color_boxes = []

    # Iterate through each letter in player's guess
    for letter in guess.upper():

        # If letter in current position of guess does not match letter at same position in answer...
        if letter != answer[position]:

            # If letter is found at another position in answer, display yellow box
            if letter in answer.upper():
                color_boxes.append("🟨")

            # If letter is not found at another position in answer, display white box
            if letter not in answer.upper():
                color_boxes.append("⬜")

        # If letter in current position of guess matches letter at same position in answer, display green box
        if letter == answer[position]:
            color_boxes.append("🟩")

        # Increase position variable by one
        position += 1

    # Print guess with double space between each letter for readability
    print("  ".join(guess.upper()))

    # Print color boxes after cleaning up default formatting of list
    print(' '.join(color_boxes))

# If player solves answer before exhausting six guesses...
if guess.upper() == answer:
    print("\nCongrats! You solved the answer.")

# If player exhausts six guesses without solving answer...
if guess.upper() != answer:
    print("\nSorry! You ran out of guesses. The answer was " + answer + ".")