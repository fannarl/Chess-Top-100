# Verkefni unnið í samstarfi Eyþór Dan Sigurðsson og Fannar Leo Örvarsson last update 19.03.2019 [03:27 : EDS] (final version?)

#Reads the file to Dict:
def create_players_dict(filename):
    ''' Reads the given file and returns a dictionary in which the name of a chess player is the key, the value is a list: [rank, country, rating, b-year] '''
    the_dict = {} 
    try:
        file = open(filename, 'r')
        for line in file: # process each line
            temp_list = line.strip().split(';') 
            lastname, firstname = temp_list[1].split(",") # The name is one field separated by ","
            key = "{} {}".format(firstname, lastname)
            the_dict[key] = get_values(temp_list)
        file.close
    except FileNotFoundError:
        print("Error File not found")
    return the_dict

def get_values(temp_list):
    values_list = [None] * 4
    values_list[0] = temp_list[0] #rank
    values_list[1] = temp_list[2] #country
    values_list[2] = temp_list[3] #rating
    values_list[3] = temp_list[4] #by year
    return(values_list)

#Dict by countries:
def create_countries_dict(dict_players):
    '''Uses a players dictionary to creata a countries dictionary in which countries are keys and tuple of player names are values'''
    year_dict = {}
    for a_tuple in dict_players.items():
        chess_player = a_tuple[0]
        chess_player_data = a_tuple[1]
        year = chess_player_data[3]
        if year in year_dict:
            name_list = year_dict[year]
            name_list.append(chess_player)
        else:
            name_list = [chess_player]
            year_dict[year] = name_list
    return year_dict

def get_average_rating(players, dict_players):
    ''' Returns the average ratings for the given players'''
    ratings = [int(dict_players[player][2]) for player in players]
    average = sum(ratings)/len(ratings)
    return average

def print_sorted(the_dict, dict_players):
    ''' Prints information sorted on the key of the_dict '''
    sorted_dict = sorted(the_dict.items())
    for key, players in sorted_dict:
        average_rating = get_average_rating(players, dict_players)
        print("{} ({}) ({:.1f}):".format(key, len(players), average_rating))
        for player in players:
            rating = dict_players[player][2]
            print("{:>40}{:>10}".format(player, rating))

def print_header(header_str):
    print(header_str)
    dashes = '-' * len(header_str)
    print(dashes)

#Main
filename = input("Enter filename: ")
dict_players = create_players_dict(filename)
dict_countries = create_countries_dict(dict_players)
print_header("Players by birth year: ")
print_sorted(dict_countries, dict_players)
