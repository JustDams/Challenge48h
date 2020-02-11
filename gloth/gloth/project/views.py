import os
from werkzeug import secure_filename
from flask import Flask, request, redirect, url_for, render_template, flash

app = Flask(__name__)
app.config.from_object("project.config.Config")

from .forms import *
from .utils import *

@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    form = PatientForm()

    if request.method == "POST":
        if form.validate() == False:
            flash("All fields are required.")
            return render_template("index.html", title="Gloth", subtitle="test", patient_form=form, name="Ynov")
        else:
            data = request.args.get(form)
            return redirect(url_for('medic'), data=data)

    return render_template("index.html", title="Gloth", subtitle="subtitle", patient_form=form, name="Ynov")


@app.route('/medic', methods=["GET","POST"])
def medic():
    form = MedicForm(request.form)
    patho_id = (request.form.get("pathology"))
    patho = getPathologyName(patho_id)
    user_id = (request.form.get("user"))
    username = getUsername(user_id)

    icd10 = getPathologyIcd10(patho_id)
    idmolecule = getTreatmentMoleculeId(icd10)

    arrayIdMol = idmolecule.replace("[","").replace("]","").split(" ")
    arrayMed = []
    arrayMol = []

    for i in range(0,len(arrayIdMol)-1):
        if arrayIdMol[i] != 'None':
            arrayMol += getMolecules(arrayIdMol[i])
            arrayMed.append(str(getMedicaments(arrayIdMol[i])).replace("[","").replace("]",""))

    form.molecule.

    return render_template("medic.html",name = "Ynov",pathology = patho,username = username,medic_form = form, arrayMed=arrayMed)