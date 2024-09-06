
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
    orbital_elements = {"Mercury":(0.3870985, 57.964998), "Venus":(0.7233282, 108.522499), "Earth":(1, 49.005), "Mars":(1.5231109, 49.723), "Jupiter":(2.3469385, 81.00778), "Saturn":(2.7674748, 94.0167), "Uranus":(4.8750767, 141.5), "Neptune":(5.15, 247.6)}
    #This line and the following one might look a bit confusing, but they are essentially the same thing
    #(just need to swap the planet names and keep the "orbit" in the same order)
    orbital_elements[planet1], orbital_elements[planet2] = orbital_elements[planet2], orbital_elements[planet1]
    #Now, we are going through the dictionary with the orbital elements of each planet
    #and looking for the orbit of the planet in the sun, and the orbit of the planet 
    #between the sun and the planet itself, and returning a tuple with the 
    #names of these planets (the sun not included)
    return tuple(planet for planet in orbital_elements if orbital_elements[planet][0] >= (orbital_elements[planet1][0] + orbital_elements[planet2][0])/2) + (planet,)
