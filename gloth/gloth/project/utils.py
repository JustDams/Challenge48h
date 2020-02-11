import os
from .models import *

### Renvoie la liste de toutes les maladies
def pathologyChoices():

    temp = Pathology.query.with_entities(Pathology.id, Pathology.name, Pathology.other_name).all()
    other_name_temp = []

    for x in temp:
        if x[2]:
            array = x[2].split(",")

            for i in range(len(array)):
                if array[i] is not None:
                    other_name_temp.append((x[0], array[i].strip()))

    choices = [(x[0], x[1]) for x in temp] + other_name_temp

    i = 0
    l = len(choices)
    while (i < l and choices[i]):
        if choices[i][1] == '':
            del choices[i]
            l -= 1
        else:
            i += 1

    return choices

#renvoie la liste de tous les users
def userChoices():

    temp = User.query.with_entities(User.id, User.forename).all()
    choices = [(x[0], x[1]) for x in temp]
    return choices

def getUsername(userid):
    user =  User.query.filter_by(id=userid).first_or_404().forename
    return user

def cleanChar(string):
    string = str(string).replace("(",'').replace(")",'').replace("'",'').replace(",",'')
    return string

#PATHOLOGY
def getPathologyDescription(pathology):#description
    desc = Pathology.query.filter_by(id=pathology).with_entities(Pathology.description).first()
    desc = cleanChar(desc)
    return desc

def getPathologyName(pathology):#name
    name = Pathology.query.filter_by(id=pathology).with_entities(Pathology.name).first()
    name = cleanChar(name)
    return name

def getPathologyIcd10(pathology):#icd10
    icd10 = Pathology.query.filter_by(id=pathology).with_entities(Pathology.icd_10).first()
    icd10 = cleanChar(icd10)
    return icd10

#TREATMENTCLA
def getTreatmentClassName(icd_10x):#pathology name
    name = TreatmentClass.query.filter_by(icd_10=icd_10x).with_entities(TreatmentClass.pathology_name).all()
    name = cleanChar(name)
    return name

#TREATMENTMOLECULE
def getTreatmentMoleculeName(icd_10x):#pathology name
    name = TreatmentMolecule.query.filter_by(icd_10=icd_10x).with_entities(TreatmentMolecule.pathology_name).all()
    name = cleanChar(name)
    return name

#TREATMENTMOLECULE
def getTreatmentCisName(icd_10x):#pathology name
    name = TreatmentCis.query.filter_by(icd_10=icd_10x).with_entities(TreatmentCis.pathology_name).all()
    name = cleanChar(name)
    return name

def getTreatmentMoleculeId(icd10):
    id = TreatmentMolecule.query.filter_by(icd_10=icd10).with_entities(TreatmentMolecule.molecule_id).all()
    id = cleanChar(id)
    return id

def getMedicaments(id):
    names = Medication.query.filter_by(molecule_id=id).with_entities(Medication.name).all()
    return names

def getMolecules(id):
    names = Molecule.query.filter_by(id=id).with_entities(Molecule.name).all()
    return names