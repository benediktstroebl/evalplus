
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
    #firstly i need to make a list of the planets
    list_of_planets = ["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"]
    #then i need to create an empty tuple to save the planets between the first planet and the second planet
    list_of_planets_between_planets = ()
    #then i need to make a for loop to check if the list of planets contains the first planet and if it does
    #then i need to add the first planet to the list of planets between the planets
    for i in range(len(list_of_planets)):
        if list_of_planets[i] == planet1:
            list_of_planets_between_planets = list_of_planets[i]
    #then i need to make a for loop to check if the list of planets contains the second planet and if it does
    #then i need to add the first planet to the list of planets between the planets
    for i in range(len(list_of_planets)):
        if list_of
