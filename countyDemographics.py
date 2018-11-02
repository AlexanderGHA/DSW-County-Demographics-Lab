import json
import operator

def main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    print(alphabetically_first_county(counties))
    print(county_most_under_18(counties))
    print(percent_most_under_18(counties))
    print(most_under_18(counties))
    print(state_with_most_counties(counties))
    print(highest_house_density(counties))
    
def alphabetically_first_county(counties):
    """Return the county with the name that comes first alphabetically."""
    count = []
    for c in counties:
        count.append(c["County"])
    return sorted(count, key=str.lower)[0]

def high_18(counties):
    idx = 0
    for i in range(len(counties)):
        if counties[i]["Age"]["Percent Under 18 Years"] > counties[idx]["Age"]["Percent Under 18 Years"]:
            idx = i
    return counties[idx]["County"], counties[idx]["State"], counties[idx]["Age"]["Percent Under 18 Years"]
    
def county_most_under_18(counties):
    """Return the name and state of a county ("<county name>, <state>") with the highest percent of under 18 year olds."""
    a, b, c = high_18(counties)
    return a + ", " + b

    
def percent_most_under_18(counties):
    """Return the highest percent of under 18 year olds."""
    a, b, c = high_18(counties)
    return c

    
def most_under_18(counties):
    """Return a list with the name and state of a county ("<county name>, <state>") and the percent of under 18 year olds for a county with the highest percent of under 18 year olds."""
    a, b, c = high_18(counties)
    return a + ", " + b + ": " + str(c)
    
def state_with_most_counties(counties):
    """Return a state that has the most counties."""
    #Make a dictionary that has a key for each state and the values keep track of the number of counties in each state
    states = {}
    
    #Find the state in the dictionary with the most counties
    for c in counties:
        state = c["State"]
        if state in states:
            states[state] += 1
        else:
            states[state] = 1
    
    #Return the state with the most counties
    state = sorted(states.items(), key=operator.itemgetter(1))[len(states)-1]
    return state[0] + ": " + str(state[1])
    
def highest_house_density(counties):
    """Compute and return an interesting fact using the demographic data about the counties in the US."""
    #[Housing][Persons per Household]
    idx = 0
    for i in range(len(counties)):
        if counties[i]["Housing"]["Persons per Household"] > counties[idx]["Housing"]["Persons per Household"]:
            idx = i
    return counties[idx]["County"] + ", " + counties[idx]["State"] + ": " + str(counties[idx]["Housing"]["Persons per Household"])
    

if __name__ == '__main__':
    main()
