import random

class Patient:
    def __init__(s, pn, pp, pa, pd, pid):
        s.pn = pn 
        s.pp = pp
        s.pa = pa
        s.pd = pd
        s.pid = pid

    def show_problem(s):
        print(f"\nPatient Problem: {s.pp} at {s.pd}")

class Specialization:
    def __init__(s, name, cond, diagno, medicines):
        s.name = name
        s.conditions = cond
        s.diagnostics = diagno
        s.medicines = medicines

doctor_names = [
    "Mehta", "Kumar", "Sharma", "Varma", "Prem",
    "Reddy", "Joshna", "Shiva", "Vijay", "Rao"
]

common_specializations = [
    Specialization("General Physician", ["Fever", "Infections", "Hypertension", "Headaches"],
                   ["CBC", "Blood Sugar", "Urinalysis"],["Febrilin", "Infexol", "Tensiva"]),
    Specialization("Cardiologist", ["Heart Diseases", "Chest Pain"],
                   ["ECG", "Echocardiogram", "Angiography"],["Cardiovex", "Angiostat", "Rhythmedol"]),
    Specialization("Dermatologist", ["Acne", "Eczema", "Fungal Infections"],
                   ["Skin Scraping", "Biopsy", "Dermoscopy"],["Acnetin", "Fungocure", "Eczemol"]),
    Specialization("Gynecologist", ["Menstrual Issues", "Pregnancy", "PCOD"],
                   ["Pelvic Ultrasound", "PAP Smear", "Hormone Tests"],["Gynovita", "Fertibol", "Prenasure"]),
    Specialization("Pediatrician", ["Child Growth", "Infections"],
                   ["Growth Charting", "CBC", "Developmental Screening"],["Growvax", "Infantol", "Chilvit"]),
    Specialization("Orthopedic Surgeon", ["Back Pain", "Fractures", "Arthritis"],
                   ["X-rays", "MRI", "CT Scan (Bones)", "Bone Densitometry"],["Bonemend", "Arthrocin", "Flexogel"]),
    Specialization("Neurologist", ["Neurological disorder","Seizures", "Stroke"],
                   ["MRI Brain", "CT", "EEG", "Nerve Conduction Test"],["Neurozil", "Migracure", "Cognitol"]),
    Specialization("Endocrinologist", ["Diabetes", "Thyroid Disorders", "Hormonal Imbalances"],
                   ["HbA1c", "Thyroid Profile (T3/T4/TSH)", "Insulin Levels"],["Glycostat", "Thyronil", "Insumix"]),
    Specialization("Pulmonologist", ["Asthma", "Cough", "Breathlessness","Pneumonia"],
                   ["Chest X-ray", "PFT", "Sputum Test", "CT Chest"],["Bronchicure", "Mucorid", "Pulmovent"]),
    Specialization("ENT Specialist", ["Ear Pain", "Sinusitis", "Sore Throat"],
                   ["Audiometry", "Nasal Endoscopy", "Tympanometry"],["Otoclear", "Nasalin", "Throacil"])
]      

class Bill:
    def __init__(s, patient, doctor, specialization, medicines, diagnostics):
        s.patient = patient
        s.doctor = doctor
        s.specialization = specialization
        s.medicines = medicines
        s.diagnostics = diagnostics
        s.consultation_fee = 2000

    def generate(s):
        print("\n-------------- BILL RECEIPT --------------")
        print(f"Patient: {s.patient.pn}")
        print(f"Age: {s.patient.pa}")
        print(f"OP Number: {s.patient.pid}")
        print(f"Date: {s.patient.pd}")
        print(f"Doctor: Dr. {s.doctor}")
        print(f"Specialization: {s.specialization}")

        print("\nDiagnosis Report:")
        for test in s.diagnostics:
            print(f" - {test}")

        print("\nMedicines Prescribed:")
        total_medicine_cost = 0
        for med, instruction, cost in s.medicines:
            print(f" - {med} ({instruction}) - ₹{cost}")
            total_medicine_cost += cost

        total = s.consultation_fee + total_medicine_cost
        print(f"\nConsultation Fee: ₹{s.consultation_fee}")
        print(f"Medicine Total: ₹{total_medicine_cost}")
        print(f"TOTAL BILL: ₹{total}")
        print("-----------------------------------\n")

if __name__ == "__main__":
    p_details = {
        "pn": input('Enter patient name: '),
        "pp": input("Enter problem: "),
        "pa": int(input("Enter age: ")),
        "pid": int(input("Enter OP number: ")),
        "pd": input("Enter date(dd/mm/year): ")
    }
    p = Patient(**p_details)

    match_found = False
    for spec in common_specializations:
        if any(p.pp.lower() == c.lower() for c in spec.conditions):
            doctor_name = random.choice(doctor_names)
            print(f"\nReferred to: Dr. {doctor_name} \nSpecialization: {spec.name}")
            print("\nDiagnosis Report:")
            for test in spec.diagnostics:
                print(f" - {test}")
            prescribed_meds = random.sample(spec.medicines, k=random.randint(1, len(spec.medicines)))
            dosages = ["1 tab", "2 tabs", "1 spoon"]
            frequencies = ["once a day", "twice a day", "after meals", "before sleep"]
            durations = ["for 5 days", "for 1 week", "for 10 days"]
            cost_range = (100, 1000)

            prescription_details = []
            print("\nPrescription:")
            for idx, med in enumerate(prescribed_meds, 1):
                dose = random.choice(dosages)
                freq = random.choice(frequencies)
                duration = random.choice(durations)
                instruction = f"{dose}, {freq}, {duration}"
                cost = random.randint(*cost_range)
                print(f" {idx}. {med} - {instruction} (₹{cost})")
                prescription_details.append((med, instruction, cost))

            match_found = True
            
            outcome = random.choice(["Cured", "Medical Management", "Cured"])
            if outcome == "Cured":
                p.pp = outcome
                p.show_problem()

                bill = Bill(p, doctor_name, spec.name, prescription_details, spec.diagnostics)
                bill.generate()
            else:
                print(f"\n{p.pn} treatment is {outcome} (Managing health, diagnosis, planning, and monitoring)")

            break

    if not match_found:
        print("No matching specialization found.")
