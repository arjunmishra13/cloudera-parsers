import hashlib
def printmd5sum(name):
  print hashlib.md5(name.encode("utf-8")).hexdigest()

if __name__ == "__main__":
  customer_name = "China Merchants Bank Co., Ltd."

  printmd5sum(customer_name)