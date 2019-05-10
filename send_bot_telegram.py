#!/usr/bin/env python3.6

import requests
import os
import sys
import time

def telegram_send_to(CHAT_ID, CONTENT_DETAIL, API_TELEGRAM):
        header={'Content-Type': 'application/json'}
        body="""{
                        "chat_id":\""""+str(CHAT_ID)+"""\",
                        "text":\""""+CONTENT_DETAIL+"""\"
                        }"""
        r=requests.post(API_TELEGRAM,data=body,headers=header,timeout=30)
        return r.content

if __name__ == '__main__':

        LINKS_CONTENT="http://www.digiboy.ir"
        NAME_PROGRAM_FILE_JAVA="digiboy.jar"
        NAME_LOG_EXPORT_RUN_JAVA="digiboy.log"
        NAME_LINK_EXPORT_UPDATE_RUN_BASH="/database-links-updated"
        NAME_LINK_EXPORT_UPDATE_RUN_BASH_OLD="/database-links-old"

        GET_PATH_CURRENT_EXECUTE_DIRECTORY = os.path.dirname(os.path.realpath(sys.argv[0]))
        GET_DIRECTORY_PATH_FILE_DATABASE_UPDATED = GET_PATH_CURRENT_EXECUTE_DIRECTORY + NAME_LINK_EXPORT_UPDATE_RUN_BASH

#        print('Directory la: ' + GET_PATH_CURRENT_EXECUTE_DIRECTORY)
#        print('File updated la: ' + GET_DIRECTORY_PATH_FILE_DATABASE_UPDATED)

        GET_DIRECTORY_PATH_FILE_DATABASE_OLD = GET_PATH_CURRENT_EXECUTE_DIRECTORY + NAME_LINK_EXPORT_UPDATE_RUN_BASH_OLD
#        print('File updated la: ' + GET_DIRECTORY_PATH_FILE_DATABASE_OLD)

# Đây là API của bot telegram

        API_TELEGRAM = 'https://api.telegram.org/bot733443322:aaGpzMtahwY_pcOg-f2-C-SAtn567ggttj8/sendMessage'
        CHAT_ID = '-917099345'
        LINKS_PAGE_WEB = ''

#       rm -rf
        os.system("rm -rf " + GET_PATH_CURRENT_EXECUTE_DIRECTORY + "/" + NAME_LOG_EXPORT_RUN_JAVA)

#       run application java

        os.system("java -jar " + GET_PATH_CURRENT_EXECUTE_DIRECTORY + "/" + NAME_PROGRAM_FILE_JAVA + " 20 >> " + GET_PATH_CURRENT_EXECUTE_DIRECTORY + "/" + NAME_LOG_EXPORT_RUN_JAVA)

#       mv "$CURRENT_DIR"/"$NAME_LINK_EXPORT_UPDATE_RUN_BASH" "$CURRENT_DIR"/"$NAME_LINK_EXPORT_UPDATE_RUN_BASH_OLD"
        if os.path.isfile(GET_DIRECTORY_PATH_FILE_DATABASE_UPDATED):
                os.system('mv -if ' + GET_DIRECTORY_PATH_FILE_DATABASE_UPDATED + " " + GET_DIRECTORY_PATH_FILE_DATABASE_OLD)
        else:
                os.system("cat " + GET_PATH_CURRENT_EXECUTE_DIRECTORY + "/" + NAME_LOG_EXPORT_RUN_JAVA + " | grep " + LINKS_CONTENT + "> " + GET_DIRECTORY_PATH_FILE_DATABASE_UPDATED)
                os.system('mv -if ' + GET_DIRECTORY_PATH_FILE_DATABASE_UPDATED + " " + GET_DIRECTORY_PATH_FILE_DATABASE_OLD)

# cat "$CURRENT_DIR"/"$NAME_LOG_EXPORT_RUN_JAVA".log | grep "$LINKS_CONTENT" > "$CURRENT_DIR"/"$NAME_LINK_EXPORT_UPDATE_RUN_BASH"
        os.system("cat " + GET_PATH_CURRENT_EXECUTE_DIRECTORY + "/" + NAME_LOG_EXPORT_RUN_JAVA + " | grep " + LINKS_CONTENT + "> " + GET_DIRECTORY_PATH_FILE_DATABASE_UPDATED)

# Add line in file database updated into list
        link_update_new = list()
        with open (GET_DIRECTORY_PATH_FILE_DATABASE_UPDATED, "r") as update_new:
                for line in update_new:
                        link_update_new.append(line.strip())
        update_new.close()

# Add line in file database old into list
        link_update_old = list()
        with open(GET_DIRECTORY_PATH_FILE_DATABASE_OLD, "r") as update_old:
                for line in update_old:
                        link_update_old.append(line.strip())
        update_old.close()

# Comparing string find links web new
        for links_new in link_update_new:
                flags = 'true'
                for links_old in link_update_old:
                        if links_new == links_old:
                                flags = 'false'
                                break;
                if flags == 'true':
                        LINK_FIND_URL_WEB = links_new
                        CONTENT_DETAIL = LINKS_PAGE_WEB + LINK_FIND_URL_WEB
                        telegram_send_to(CHAT_ID, CONTENT_DETAIL, API_TELEGRAM)
                        time.sleep(120)
                        #print(CONTENT_DETAIL)
