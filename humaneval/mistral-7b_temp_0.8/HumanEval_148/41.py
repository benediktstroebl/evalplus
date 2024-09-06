
def bf(planet1, planet2):
    '''
    There are eight planets in our solar system: the closerst to the Sun 
    is Mercury, the next one is Venus, then Earth, Mars, Jupiter, Saturn, 
    Uranus, Neptune.
    Write a function that takes two planet names as strings planet1 and planet2. 
    The function should return a tuple containing all planets whose orbits are 
    located between the orbit of planet1 and the orbit of planet2, sorted by 
    the proximity to the sun. 
    The function should return an empty tuple if planet1 or planet2
    are not correct planet names. 
    Examples
    bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
    bf("Earth", "Mercury") ==> ("Venus")
    bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    '''
    # YOUR CODE GOES HERE
    # this list should contain all the planet names
    planet_list = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

    # here we search for the index of the planet 
    # the search returns -1 if the planet is not in the list
    planet1_index = planet_list.index(planet1)
    planet2_index = planet_list.index(planet2)

    # here we create a list that will contain the planets between planet1 and planet2
    between_planets = []

    # this loop will create all the planets between the two
    # we use the index from above
    for i in range(planet1_index, planet2_index + 1):
        between_planets.append(planet_list[i])

    # now we have to check if the tuple is empty 
    # we check for the first planet to be in the list
    if planet1_index == -1:
       
