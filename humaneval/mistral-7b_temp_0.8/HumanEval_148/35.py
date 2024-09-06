
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
    #your code here
    #print("orbit",orbit)
    l=[]
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    #planet1 = "Earth"
    #planet2 = "Mercury"

    if planet1 in planets and planet2 in planets:



        if planet1==planet2:
            print("orbits of planet",planet1,"and",planet2,"are the same")
            return tuple()
        elif planet1=="Mercury":
            l.append(planet1)
            #print("l",l)
        elif planet1=="Venus":
            l.append(planet1)
            #print("l",l)
        elif planet1=="Earth":
            l.append(planet1)
            #print("l",l)
        elif planet1=="Mars":
            l.append(planet1)
            #print("l",l)
