from wsgiref.validate import validator
#from wsgiref.simple_server import make_server

# Our callable object which is intentionally not compliant to the
# standard, so the validator is going to break
def simple_app(environ, start_response):
    status = '200 OK'  # HTTP Status
    headers = [('Content-type', 'text/plain')]  # HTTP Headers
    start_response(status, headers)

    # This is going to break because we need to return a list, and
    # the validator is going to inform us
    return b"Hello World"

# This is the application wrapped in a validator
validator_app = validator(simple_app)

#with make_server('', 8000, validator_app) as httpd:
#    print("Listening on port 8000....")
#    httpd.serve_forever()

#def application(env, start_response):
#    start_response('200 OK', [('Content-Type','text/html')])
#    return [b"Hello World"]

def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    yield b'''
 <!DOCTYPE html>
 <html>
   <head>
     <title> Welcome! </title>
     <!--link rel="stylesheet" type="text/css" href="base.css"-->
   </head>
   <body>
     <p> Welcome to PikeSquares! </p>
     <p>

                            ++                                      
                          +++++                                     
                         +++++++                                    
                         +++++++                                    
                         +++++++                                    
                         +++++++                                    
                       +++++++++++++                                
                    ++++++++++++++++++                              
                    +++++++++++++++++++                             
                    +++++++++++++++++++                             
                    ++++++++++++++++++++++                          
                    ++++++++++++++++++++++                          
                    ++++++++++++++++++++++                          
                   +++++++++++++++++++++++         PikeSquares is now installed        
                   +++++++++++++++++++++++                          
                   +++++++++++++++++++++++              
                   +++++++++++++++  ++++++             Run `pikesquares up` to launch              
                   +++++++++++++++++++++++                       
                  ++++++++++++++++++++++++                      or    
                  ++++++++++++++++++++++++                  
                  +++++++++++++++++++ ++++                 `pikesquares --help` for commands
                 +++++++++++++++++++++ ++                           
                 +++++++++++++++++++++  +                           
                +++ ++++++++++++++++++                              
              +++   +++++++++++++++++++                             
             ++     +++++++++++++++++ +                             
           +++      +++++++++++++++++ +                             
          ++        ++++++++++++++++++ +                            
        +++         ++++++++++++++++++ +                            
       ++           +++++++++++++++++++++                           
     ++             +++++++++++++++++++++                           
    ++                  ++++++    +++++++                           
  ++                     ++++      +++++ +                          
 +                       ++++       ++++++                          
                         ++++        ++++                           
                        +++++        ++++                           
                      +++++++        ++++                           
                   ++++++++++        +++++                          


     </p>
   </body>
 </html>'''
