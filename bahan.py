
                
        if op.type == 19:
            if wait["ghost"] == True:
                try:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        G = random.choice(ABC).getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        random.choice(ABC).updateGroup(G)
                        Ticket = random.choice(ABC).reissueGroupTicket(op.param1)                                     
                        sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                        sw.kickoutFromGroup(op.param1,[op.param2])
                        sw.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid])
                        sw.leaveGroup(op.param1)
                        X = kf.getGroup(op.param1)
                        kf.updateGroup(X)
                        X.preventedJoinByTicket = True
                        kf.inviteIntoGroup(op.param1,[Zmid,Jmid])
                        wait["blacklist"][op.param2] = True
                except:
                    pass
                
        if op.type == 32:
            if wait["cancel"] == True:
              if op.param3 in Bots:    
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(ABC).inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Jmid,Zmid])
                    except:
                        pass
                                                    

        if op.type == 13:
            if op.param3 in wait["blacklist"]:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = cl.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            if _mid not in Bots:
                                random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass
                                                    

        if op.type == 13:
            if op.param2 in wait["blacklist"]:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = cl.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            if _mid not in Bots:
                                random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass
                        
        if op.type == 19:
            if mid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])                 
                        ki.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid])
                        cl.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            kk.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid])
                            cl.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid])
                                cl.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                    kb.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid])
                                    cl.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        kd.kickoutFromGroup(op.param1,[op.param2])
                                        kd.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid])
                                        cl.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = ki.getGroup(op.param1)
                                            G.preventedJoinByTicket = False                           
                                            ki.kickoutFromGroup(op.param1,[op.param2])
                                            ki.updateGroup(G)
                                            Ticket = ki.reissueGroupTicket(op.param1)                                 
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = ki.getGroup(op.param1)
                                            G.preventedJoinByTicket = True                  
                                            Ticket = ki.reissueGroupTicket(op.param1)                   
                                            ki.updateGroup(G)
                                        except:
                                            try:
                                                kk.kickoutFromGroup(op.param1,[op.param2])
                                                kk.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid])
                                                cl.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                                    kc.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid])
                                                    cl.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                                        kb.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid])
                                                        cl.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            kj.acceptGroupInvitation(op.param1)       
                                                            G = kj.getGroup(op.param1)
                                                            G.preventedJoinByTicket = False   
                                                            kj.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid])     
                                                            cl.acceptGroupInvitation(op.param1)
                                                            cl.kickoutFromGroup(op.param1,[op.param2])
                                                            ki.acceptGroupInvitation(op.param1)
                                                            ki.kickoutFromGroup(op.param1,[op.param2])
                                                            kk.acceptGroupInvitation(op.param1)
                                                            kk.kickoutFromGroup(op.param1,[op.param2])
                                                            kc.acceptGroupInvitation(op.param1)
                                                            kc.kickoutFromGroup(op.param1,[op.param2])
                                                            kb.acceptGroupInvitation(op.param1)
                                                            kb.kickoutFromGroup(op.param1,[op.param2])
                                                            kd.acceptGroupInvitation(op.param1)
                                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                                            ke.acceptGroupInvitation(op.param1)
                                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                                            kf.acceptGroupInvitation(op.param1)
                                                            kf.kickoutFromGroup(op.param1,[op.param2])
                                                            kj.leaveGroup(op.param1)
                                                            X = kf.getGroup(op.param1)
                                                            X.preventedJoinByTicket = True
                                                            kf.inviteIntoGroup(op.param1,[Jmid,Zmid])
                                                            wait["blacklist"][op.param2] = True        
                                                        except:
                                                            pass
                return