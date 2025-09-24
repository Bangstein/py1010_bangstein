"""

Arbeidskrav 1: Sammenlikning av årlige kostnader for elbil og bensinbil
Bjornar Bangstein (bbangst@gmail.com)
Updated 2025 09 24

"""


#----[ GENERELL INFORMASJON ]----
km_år = 10000                   # [km/år] kjørelengde
tf_avgift = 8.38                # [kr/dag] trafikkforsikringsavgift
tf_avgift_år = tf_avgift*365    # [kr/år] trafikkforsikringsavgift per år


#----[ EL KOSTNADER ]----
el_forsikring = 5000            # [kr/år] forsikring elbil
el_forbruk = 0.2                # [kWh/km] drivstofforbruk
el_strømpris = 2.00             # [kr/kWh] strømpris
el_bom = 0.1                    # [kr/km] bomavgift per km elbil

el_strøm_år = (el_forbruk)*(km_år)*(el_strømpris)                             # [kr/år] strømkostnad per år
el_bom_år = (el_bom)*(km_år)                                                  # [kr/år] bomavgift elbil per år
el_tot_år = (el_strøm_år) + (el_bom_år) + (tf_avgift_år) + (el_forsikring)    # [kr/år] total elbilkostnad per år


#----[ BENSIN KOSTNADER ]----
ben_forsikring = 7500           # [kr/år] forsikring bensinbil
ben_forbruk = 1.0               # [kr/km] bensinforbruk per år
ben_bom = 0.3                   # [kr/km] bomavgift per km bensinbil

ben_forbruk_år = (ben_forbruk)*(km_år)                                              # [kr/år] drivstoffkostnad per år
ben_bom_år = (ben_bom)*(km_år)                                                      # [kr/år] bompenger per år 
ben_tot_år = (ben_forbruk_år) + (ben_bom_år) + (tf_avgift_år) + (ben_forsikring)    # [kr/år] total bensinbilkostnad per år


#----[ SAMMENLIKNING ]----
diff = abs(ben_tot_år - el_tot_år)    # [kr] kostnadsdifferanse mellom elbil og bensinbil
print('Bensinbil årlig kostnad = {:.1f}'.format(ben_tot_år))
print('Elbil årlig kostnad = {:.1f}'.format(el_tot_år))
print('Årlig kostnadsdifferanse = {}'.format(diff))
