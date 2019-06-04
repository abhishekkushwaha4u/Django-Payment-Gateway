from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from . import checksum
# Create your views here.

class startpayment(View):
    parameters = {
        "MID": "DIY12386817555501617",
        "ORDER_ID": "Abhi123456",
        "CUST_ID": "NewCustomer12345",
        "TXN_AMOUNT": "350",
        "CHANNEL_ID": "WEB",
        "INDUSTRY_TYPE_ID": "Retail",
        "WEBSITE": "DIYtestingweb",
        "CALLBACK_URL":"http://127.0.0.1:8000/handlerequest/",
    }
    parameters['CHECKSUMHASH']=checksum.generate_checksum(parameters,"bKMfNxPPf_QdZppa")

    def get(self,request):
        parameters = {
        "MID": "DIY12386817555501617",
        "ORDER_ID": "Abhi12345624",
        "CUST_ID": "NewCustomer1234564",
        "TXN_AMOUNT": "350",
        "CHANNEL_ID": "WEB",
        "INDUSTRY_TYPE_ID": "Retail",
        "WEBSITE": "DIYtestingweb",
        "CALLBACK_URL":"http://127.0.0.1:8000/handlerequest/",
        }
        parameters['CHECKSUMHASH']=checksum.generate_checksum(parameters,"bKMfNxPPf_QdZppa")

        return render(request,"Payments/paytm.html",{"parameters":parameters})




class handle_request(View):
    def post(self,request):
        form = request.POST
        response = {}
        for i in form.keys():
            response[i]=form[i]
            if i=="CHECKSUMHASH":
                newchecksum=form[i]
        verify = checksum.verify_checksum(response,"bKMfNxPPf_QdZppa",newchecksum)
        if verify:
            if response['RESPCODE']=='01':
                print(response)
                return HttpResponse("Success!")
            else:
                print(response)
                return HttpResponse("Transanction Failed!")
        else:
            return HttpResponse("Invalid Session!")
    
    

