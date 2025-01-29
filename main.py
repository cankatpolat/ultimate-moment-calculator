
try:

    import math
    concrete = input("Concrete is C30 Concrete (Y/N)? :").strip().upper()
    steel = input("Steel is S420 Steel (Y/N)? :").strip().upper()

    if concrete == "Y" and steel == "Y":
        k1 = 0.82
        areaSteel = float(input("Enter the area of steel (Ast) :"))
        d = float(input("Enter the length of the section (d): "))
        b = float(input("Enter the top width of the section (b): "))
        bw = float(input("Enter the above width of the section (bw): "))
        hf = float(input("Enter the hf value:"))
        Fs = areaSteel * 3650
        Fc0 = 0.85 * 200 * b * hf
        c = (0.85 * 200 * b * k1) / (areaSteel * 3650)
        if k1 * c < hf:
                Fc = 0.85 * 200 * b * k1 * c
                z = d - ((k1 * c) / 2)
                Mu = round(Fc * z, 2)
                print(f"Ultimate Moment Capacity is {round(Mu, 2)}")
        elif k1 * c > hf:
                Fc2 = 0.85 * 200 * (b-bw) * hf
                c1 = (areaSteel * 3650 - Fc2) / (0.85 * 200 * bw * k1)
                Fc1 = 0.85 * 200 * bw * k1 * c1
                z = d - ((k1 * c1) / 2)
                z0 = d - (hf / 2)
                Mu = (Fc1 * z) + (Fc2 * z0)
                print(f"Ultimate Moment Capacity is {round(Mu, 2)}")

        else:
            print("Please give the relative numbers correctly!")


    else:
        print("Concrete must be C30 and Steel must be S420")


except ValueError:
    print("Answers must be only Y and N!")
