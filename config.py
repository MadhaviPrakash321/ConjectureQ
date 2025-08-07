
SEED              = 31415           # reproducibility for torch & numpy  lollol you dont want the "performance increase" to be due to a new random trajectory that the optimizer takes....
BATCH_SIZE        = 64
SGD_LR            = 0.01
EPOCHS            = 5
PASS_THRESHOLD    = 0.92            # accuracy required for a solver to “pass”
KLD_BINS          = 32              # histogram resolution for symmetric-KL
DEVICE            = "cuda" if __import__("torch").cuda.is_available() else "cpu"
