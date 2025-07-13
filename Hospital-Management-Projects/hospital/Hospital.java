import java.util.*;
class Patient
{
	String pname,prblm;
	int pamt;
	void showPat()
	{
		System.out.println("\nPatient name: "+pname+" \nProblem: "+prblm+" \namt: ₹"+pamt);
	}
}

class Doctor
{
	String dname,sep;
	int damt;
	void showDoc()
	{
		System.out.println("\nDoctor name: "+dname+" \nSpe: "+sep+" \namt: ₹"+damt);
	}	
	void treatment(Patient x)
	{
		x.prblm="Cured";
		x.pamt-=250;
		damt+=250;
	}
}

class Pharma
{
	String phname;
	float phamt;
	int phfee=1000;
	void showPh()
	{
		System.out.println("\nPharmacy name: "+phname+" \namt: ₹"+phamt);
	}	
	void medical(Patient x, Doctor y)
	{
		x.pamt-=phfee;
		y.damt+=phfee*0.4;
		phamt+=phfee*0.6;
	}
}

class Diagno
{
	String diname;
	int difee=2000;
	float diamt;
	void showDi()
	{
		System.out.println("\nDiagnostics name: "+diname+" \namt: ₹"+diamt);
	}	
	void diagnosis(Patient x, Doctor y)
	{
		x.pamt-=difee;
		y.damt+=difee*0.4;
		diamt+=difee*0.6;
	}
}

class Hospital {
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		Doctor d=new Doctor();
		Pharma ph=new Pharma();
		Diagno di=new Diagno();
		int n;
		System.out.println("Enter no.of patients: ");
		n=sc.nextInt();
		sc.nextLine();
		Patient p[]=new Patient[n];
		for(int i=0;i<n;i++)
		{
			p[i]=new Patient();
			System.out.println("Enter Patient name: ");
			p[i].pname=sc.nextLine();
			System.out.println("Enter Patient problem: ");
			p[i].prblm=sc.nextLine();
			System.out.println("Enter Patient amount: ");
			p[i].pamt=sc.nextInt();
			sc.nextLine();
		}
		d.dname="Hari";
		d.sep="Gastro";
		d.damt=0;
		ph.phname="Apolo";
		ph.phamt=0;
		di.diname="Vinod diagnostics";
		di.diamt=0;
		for(int i=0;i<n;i++)
		{
			p[i].showPat();
		}
		d.showDoc();
		ph.showPh();
		di.showDi();
		for(int i=0;i<n;i++)
		{
			d.treatment(p[i]);
			ph.medical(p[i], d);
	    	di.diagnosis(p[i], d);
		}
		System.out.println("\nAfter treatment");
		for(int i=0;i<n;i++)
		{
			p[i].showPat();
		}
		d.showDoc();
		ph.showPh();
		di.showDi();
	}
}
