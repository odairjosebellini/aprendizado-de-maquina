# https://code.tutsplus.com/pt/tutorials/introduction-to-machine-learning-in-python--cms-30623
# O código abaixo vai prever resultados a partir de um determinado conjunto de dados. 
# A seguir é mostrado como prever qual animal tem uma altura de 7 polegadas, 0,6 kg de peso e uma temperatura de 41 ºC:

from sklearn import tree
features = [[7, 0.6, 40], [7, 0.6, 41], [37, 600, 37], [37, 600, 38]]
#labels = [chicken, chicken, horse, horse]
labels = [0, 0, 1, 1]
classif = tree.DecisionTreeClassifier()
classif.fit(features, labels)
 
print classif.predict([[7, 0.6, 41]])
 
#output
# [0]  or a Chicken
