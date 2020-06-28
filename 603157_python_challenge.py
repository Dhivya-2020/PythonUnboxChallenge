
import numpy as np
import random


stop_counter = 28
stop_iteration = 10000



class BoardSample:
	def __init__(self):
		self.sequence = None
		self.fitness = None
	def setSequence(self, val):
		self.sequence = val
	def setFitness(self, fitness):
		self.fitness = fitness
	    
def fitness(randomSequence = None):
	clashes = 0;
	'''there is a possibility of row clases in child inspite of the unique samples chosen for population 
        because of crossover and mutation hence the row clash check is done'''
	row_col_clashes = abs(len(randomSequence) - len(np.unique(randomSequence)))
	clashes += row_col_clashes
	for i in range(len(randomSequence)):
		for j in range(len(randomSequence)):
			if ( i != j):
				dx = abs(i-j)
				dy = abs(randomSequence[i] - randomSequence[j])
				if(dx == dy):
					clashes += 1
	return 28 - clashes	

    
def generatePopulation(population_size):

	population = [BoardSample() for i in range(population_size)]
	for i in range(population_size):
		population[i].setSequence(random.sample(range(0,8),8))
		population[i].setFitness(fitness(population[i].sequence))

	return population

def getParent():
        '''Tournament Selection - 3 random chromosomes/sequences are chosen
        out of the population and 2 of them are made parents based on fitness score'''
        
        parent1, parent2 = None, None
        
        random_number=random.sample(range(0,len(population)),3)
        option1=population[random_number[0]]
        option2=population[random_number[1]]
        option3=population[random_number[2]]

        if(option1.fitness>=option2.fitness and option1.fitness>=option3.fitness):
                parent1=option1
                parent2=option2                
        elif(option2.fitness>=option1.fitness and option2.fitness>=option3.fitness):
                parent1=option2
                parent2=option3
        else:
                parent1=option3
                parent2=option1
        return parent1,parent2

def crossover(parent1, parent2):
        '''One Point Crossover - random crossover point is selected between the numbers 3 and 6 and the parent sequences are swapped at that point'''
        c = random.randint(3,6)
        child = BoardSample()
        child.sequence = []
        child.sequence.extend(parent1.sequence[0:c])
        child.sequence.extend(parent2.sequence[c:])
        child.setFitness(fitness(child.sequence))
        return child

def mutate(child):
        '''Swap Mutation - two random positions within a sequnce are chosen and swapped'''
        mutation_points=random.sample(range(0,7),2)
        swap1=child.sequence[mutation_points[0]]
        swap2=child.sequence[mutation_points[1]]
        child.sequence[mutation_points[0]]=swap2
        child.sequence[mutation_points[1]]=swap1
        return child


def algo(iteration):
        newpopulation = []
        for i in range(len(population)):
                parent1, parent2 = getParent()
                child = crossover(parent1, parent2)
                if child.fitness>15:
                        child=mutate(child)
                newpopulation.append(child)
        return newpopulation


def stop():
	fitnessvals = [pos.fitness for pos in population]
	if stop_counter in fitnessvals:
		return True
	if stop_iteration == iteration:
		return True
	return False

population = generatePopulation(1000)


iteration = 0;
while not stop():
	population = algo(iteration)
	iteration +=1 

for each in population:
	if each.fitness == 28:
		print ('The sequence is:',each.sequence)
		break
