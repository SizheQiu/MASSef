(* Created with the Wolfram Language : www.wolfram.com *)
(metabolite["2pg", "c"]*rateconst["dPGM1", True]*
  (rateconst["dPGM2", True] + rateconst["dPGM3", False] + 
   rateconst["dPGM3", True]))/
 (rateconst["dPGM1", False]*(rateconst["dPGM2", True] + 
    rateconst["dPGM3", False]) + rateconst["dPGM2", True]*
   rateconst["dPGM3", True] + metabolite["2pg", "c"]*rateconst["dPGM1", True]*
   (rateconst["dPGM2", True] + rateconst["dPGM3", False] + 
    rateconst["dPGM3", True]))
