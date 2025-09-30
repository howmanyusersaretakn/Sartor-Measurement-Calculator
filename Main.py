def measurements(height, hip, waist):
        cl = height - 9
        cr = cl/63
        stc = cl * .635
        sthip = stc + cr
        hpd = hip - sthip
        bwl = ((2*cl/7)+(cr/2))
        outseam = cl - bwl
        cd = bwl - (7.75*cr) + (.25*hpd)
        inseam = outseam - cd
        kh = (inseam/2)+2
        qhp = hip/4
        fce = hip/16
        bce = (hip/8)+1
        bre = (((qhp+fce)/2)-(fce+.25))/2
        qw = waist/4
        dartwidth = ((hip-waist)/8)+.5
        dartlen = cd/3
        bww = qw + dartwidth

        return f"""
        cape length = {cl:.2f}
        correction ratio = {cr:.2f}
        standard chest = {stc:.2f}
        standard hip = {sthip:.2f}
        hip deviation = {hpd:.2f}
        back waist length = {bwl:.2f}
        out seam = {outseam:.2f}
        crotch depth = {cd:.2f}
        inseam = {inseam:.2f}
        knee height = {kh:.2f}
        quarter hip = {qhp:.2f}
        front crotch extension = {fce:.2f}
        back crotch extension = {bce:.2f}
        back rise extension = {bre:.2f}
        quarter waist = {qw:.2f}
        dart width = {dartwidth:.2f}
        dart length = {dartlen:.2f}
        back waist width = {bww:.2f}
        """

print("Enter height in inches: ")
height_measure = float(input())
print("Enter hip measurement in inches: ")
hip_measure = float(input())
print("Enter waist measurement in inches: ")
waist_measure = float(input())
print(measurements(height_measure, hip_measure, waist_measure))